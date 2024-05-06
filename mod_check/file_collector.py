#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import os
import time
import hashlib
import functools
import collections
from typing import Dict, List, Tuple, Set, Union

from mod_check.mod_check_singleton import ModCheckSingleton

from mod_check.modinfo import ModInfo
try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class FileCollector(metaclass=ModCheckSingleton):
    def __init__(self, the_sims_4_folder: str = None):
        if the_sims_4_folder:
            self._the_sims_4_folder = the_sims_4_folder
        else:
            self._the_sims_4_folder = os.path.dirname(os.path.abspath(__file__)).partition(f"{os.sep}Mods{os.sep}")[0]
        self._the_sims_4_mods_folder = os.path.join(self._the_sims_4_folder, 'Mods')

    @property
    def the_sims_4_folder(self):
        return self._the_sims_4_folder

    @property
    def the_sims_4_mods_folder(self):
        return self._the_sims_4_mods_folder

    def get_filenames(self) -> List[str]:
        """
        @return: All file names (including path) found in Mods
        """
        def compare(file1, file2):
            basename1 = os.path.basename(file1)
            basename2 = os.path.basename(file2)
            if basename1 < basename2:
                return -1
            else:
                return 1

        filenames: List[str] = []
        for root, dirs, files in os.walk(self.the_sims_4_mods_folder):
            for filename in files:
                filename_path = f"{os.path.join(root, filename)}"
                filename_path = filename_path.replace(f"{self.the_sims_4_mods_folder}{os.sep}", '')
                filenames.append(filename_path)
        filenames = sorted(filenames, key=functools.cmp_to_key(compare))
        return filenames

    def get_duplicate_filenames(self, filenames: List[str]) -> Set[str]:
        """
        @param filenames:
        @return: All duplicate file names (basename) found in Mods
        """
        duplicate_filenames: Union[List[str], Set[str]] = []
        for filename in filenames:
            basename = os.path.basename(filename)
            duplicate_filenames.append(basename)
        duplicate_filenames = [item for item, count in collections.Counter(duplicate_filenames).items() if count > 1]
        return duplicate_filenames

    def get_checksums(self, filenames: List[str], fast_checksums: bool = True, return_only_duplicates: bool = True):
        checksums: Dict[int, List[str]] = {}
        duplicate_checksums: Union[Set[int], List[int]] = []
        for filename in filenames:
            fn = os.path.join(self.the_sims_4_mods_folder, filename)
            with open(fn, 'rb') as fp:
                size = os.path.getsize(fn)
                if fast_checksums is False or size < 5_000_000:
                    b = fp.read()
                else:
                    # Read 4 MB
                    b = f"{size}".encode()
                    b += fp.read(1_000_000)
                    fp.seek(int(size/3))
                    b += fp.read(1_000_000)
                    fp.seek(int(size*2/3))
                    b += fp.read(1_000_000)
                    fp.seek(size - 1_000_000)
                    b += fp.read(1_000_000)
                sha1 = int(hashlib.sha1(b).hexdigest(), 16)
                current_filenames = checksums.get(sha1, [])
                current_filenames.append(filename)
                checksums.update({sha1: current_filenames})
                duplicate_checksums.append(sha1)

        if return_only_duplicates:
            duplicate_checksums = [item for item, count in collections.Counter(duplicate_checksums).items() if count > 1]
            _checksums: Dict[int, List[str]] = {}
            for duplicate_checksum in duplicate_checksums:
                _checksums.update({duplicate_checksum: checksums.get(duplicate_checksum)})
            return _checksums

        return checksums

    def get_meta_information(self, filenames: List[str], duplicate_filenames: Set[str] = None) -> Dict[str, Tuple[int, int]]:
        """
        @param filenames:
        @param duplicate_filenames: To process only duplicate file names.
        @return: Dict with all filenames (in duplicate_filenames) and a tuple with the creation time and size.
        """
        meta_information: Dict[str, Tuple[int, int]] = {}
        for filename in filenames:
            basename = os.path.basename(filename)
            if duplicate_filenames and basename not in duplicate_filenames:
                continue
            fn = os.path.join(self.the_sims_4_mods_folder, filename)
            size = os.path.getsize(fn)
            ctime = int(time.strftime('%Y%m%d%H%M%S', time.localtime(os.path.getctime(fn))))  # 19991231235959 for 1999-12-31T23:59:59
            meta_information.update({filename: (ctime, size)})
        return meta_information

    def get_inactive_scripts(self, filenames: List[str]) -> List[str]:
        """
        @param filenames:
        @return: Dict with all scripts which don't work.
        """
        inactive_scripts: List[str] = []
        for filename in filenames:
            f = filename.lower()
            if f.endswith('.ts4script') or f.endswith('.zip'):
                dir_name = os.path.dirname(filename)
                if os.sep in dir_name:
                    inactive_scripts.append(filename)
            elif f.endswith('.py'):
                dir_name = os.path.dirname(filename)
                user_dir, _, scripts = dir_name.partition(os.sep)
                if os.sep in user_dir or scripts != 'Scripts':
                    inactive_scripts.append(filename)
        return inactive_scripts

    def get_filetypes(self, filenames: List[str]) -> Set[str]:
        filetypes: Set[str] = set()
        for filename in filenames:
            filetype = filename.rpartition('.')[2]
            filetypes.add(filetype)
        return filetypes

    def get_filetypes_details(self, filenames: List[str]) -> Dict[str, List[str]]:
        filetypes: Dict[str, List[str]] = dict()
        for filename in filenames:
            filetype = filename.rpartition('.')[2]
            folder = filename.rpartition(os.sep)[0]
            current_folders = filetypes.get(filetype, [])
            current_folders.append(folder)
            filetypes.update({filetype: current_folders})
        return filetypes

    def get_mod_data_folders(self) -> Set[str]:
        mod_data_folders: Union[List[str], Set[str]] = set()
        ea_folder = os.path.dirname(self.the_sims_4_folder)
        mod_data_sep = f"{os.sep}mod_data{os.sep}"
        for root, dirs, files in os.walk(self.the_sims_4_folder):
            for filename in files:
                filename_path = f"{os.path.join(root, filename)}"
                filename_path = filename_path.replace(f"{ea_folder}{os.sep}", '')
                if mod_data_sep in filename_path:
                    a, b, c = filename_path.partition(mod_data_sep)
                    c = c.partition(f"{os.sep}")[0]
                    mod_data_folders.add(f"{a}{b}{c}")
        mod_data_folders = sorted(mod_data_folders)
        return mod_data_folders

    def get_files_to_avoid(self, filenames: List[str]) -> List[str]:
        spyware = [
            'TURBODRIVER_WickedWhims_Scripts', 'TURBODRIVER_WickedWhims_Tuning',
            'TURBODRIVER_WonderfulWhims_Scripts', 'TURBODRIVER_WonderfulWhims_Tuning',
            'mc_career', 'mc_cas', 'mc_cheats', 'mc_cleaner', 'mc_clubs', 'mc_cmd_center', 'mc_control', 'mc_dresser', 'mc_gedcom', 'mc_occult', 'mc_population', 'mc_pregnancy', 'mc_tuner', 'mc_woohoo',
            'Tmex-ModGuard',
        ]
        bad_files = [
            '=RedAppleNet=', 'AEP', 'NisaK_Wicked_Perversions',
            'Tmex-BetterExceptions', 'BodySelectorGenderUnlocks', 'simdulgence_BodySelectorGenderUnlocks',
            '[Kuttoe] HomeRegions',
        ]
        outdated_files = [
            'Cruxmyth_Customizations', 'Cruxmyth_Customizations_Volume_B', 'Cruxmyth_Customizations_Volume_C', 'Cruxmyth_Customizations_Volume_D',
        ]
        files_to_avoid: List[str] = []
        hard_coded_list_of_files_to_avoid = [f.lower() for f in [*spyware, *bad_files, *outdated_files]]
        for filename in filenames:
            basename = os.path.basename(filename).rpartition('.')[0].lower()
            if basename in hard_coded_list_of_files_to_avoid:
                files_to_avoid.append(filename)
        return files_to_avoid