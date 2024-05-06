#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from mod_check.ts4stats import TS4Stats
from mod_check.file_collector import FileCollector
from mod_check.mod_check_singleton import ModCheckSingleton


class ModCheckStore(metaclass=ModCheckSingleton):

    def __init__(self):
        self.fc = FileCollector()
        self.stats = TS4Stats()
        self._filenames = None
        self._duplicate_filenames = None
        self._duplicate_dates = None
        self._checksums_fast_dup = None
        self._checksums_fast_all = None
        self._checksums_slow_dup = None
        self._checksums_slow_all = None
        self._inactive_scripts = None
        self._filetypes = None
        self._filetype_details = None
        self._mod_data = None
        self._files_to_avoid = None
        self._available_packs = None
        self._missing_packs = None
        self._tuning_count = None
        self._instance_managers = None

    def clear(self):
        self._filenames = None
        self._duplicate_filenames = None
        self._duplicate_dates = None
        self._checksums_fast_dup = None
        self._checksums_fast_all = None
        self._checksums_slow_dup = None
        self._checksums_slow_all = None
        self._inactive_scripts = None
        self._filetypes = None
        self._filetype_details = None
        self._mod_data = None
        self._files_to_avoid = None
        self._available_packs = None
        self._missing_packs = None
        self._tuning_count = None
        self._instance_managers = None

    @property
    def filenames(self):
        if not self._filenames:
            self._filenames = self.fc.get_filenames()
        return self._filenames

    @property
    def duplicate_filenames(self):
        if not self._duplicate_filenames:
            self._duplicate_filenames = self.fc.get_duplicate_filenames(self.filenames)
        return self._duplicate_filenames

    @property
    def duplicate_dates(self):
        if not self._duplicate_dates:
            self._duplicate_dates = self.fc.get_meta_information(self.filenames, self.duplicate_filenames)
        return self._duplicate_dates

    @property
    def inactive_scripts(self):
        if not self._inactive_scripts:
            self._inactive_scripts = self.fc.get_inactive_scripts(self.filenames)
        return self._inactive_scripts

    @property
    def filetypes(self):
        if not self._filetypes:
            self._filetypes = self.fc.get_filetypes(self.filenames)
        return self._filetypes

    @property
    def filetype_details(self):
        if not self._filetype_details:
            self._filetype_details = self.fc.get_filetypes_details(self.filenames)
        return self._filetype_details

    @property
    def mod_data(self):
        if not self._mod_data:
            self._mod_data = self.fc.get_mod_data_folders()
        return self._mod_data

    @property
    def files_to_avoid(self):
        if not self._files_to_avoid:
            self._files_to_avoid = self.fc.get_files_to_avoid(self.filenames)
        return self._files_to_avoid

    @property
    def checksums_fast_dup(self):
        if not self._checksums_fast_dup:
            self._checksums_fast_dup = self.fc.get_checksums(self.filenames, fast_checksums=True, return_only_duplicates=True)
        return self._checksums_fast_dup

    @property
    def checksums_fast_all(self):
        if not self._checksums_fast_all:
            self._checksums_fast_all = self.fc.get_checksums(self.filenames, fast_checksums=True, return_only_duplicates=False)
        return self._checksums_fast_all

    @property
    def checksums_slow_dup(self):
        if not self._checksums_slow_dup:
            self._checksums_slow_dup = self.fc.get_checksums(self.filenames, fast_checksums=False, return_only_duplicates=True)
        return self._checksums_slow_dup

    @property
    def checksums_slow_all(self):
        if not self._checksums_slow_all:
            self._checksums_slow_all = self.fc.get_checksums(self.filenames, fast_checksums=False, return_only_duplicates=False)
        return self._checksums_slow_all

    @property
    def dlcs(self):
        if self._available_packs is None or self._missing_packs is None:
            self._available_packs, self._missing_packs = self.stats.get_dlcs()
        return self._available_packs, self._missing_packs

    @property
    def tuning_count(self):
        if self._tuning_count is None:
            self._tuning_count = self.stats.count_tunings()
        return self._tuning_count

    @property
    def instance_managers(self):
        if self._instance_managers is None:
            self._instance_managers = self.stats.get_instance_managers()
        return self._instance_managers

