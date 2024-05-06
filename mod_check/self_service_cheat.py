#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Set

from mod_check.modinfo import ModInfo
from mod_check.mod_check_store import ModCheckStore

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput

try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class SelfServiceCheat:

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.reset', 'Clear all data')
    def o19_debug_mc_reset(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        mcs.clear()
        output(f"Removed all data from memory.")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.filenames', 'Log all file names')
    def o19_debug_mc_duplicate_files(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        filenames = mcs.filenames
        output(f"Found {len(filenames)} files")
        log.debug(f"filenames={filenames}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.duplicate_files', 'Log all duplicate files')
    def o19_debug_mc_duplicate_files(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        duplicate_filenames = mcs.duplicate_filenames
        output(f"Found {len(duplicate_filenames)} duplicate files")
        log.debug(f"duplicate_filenames={duplicate_filenames}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.duplicate_dates', 'Log all duplicate files with date and size')
    def o19_debug_mc_duplicate_dates(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        duplicate_dates = mcs.duplicate_dates
        output(f"Found {len(duplicate_dates)} duplicate files")
        log.debug(f"duplicate_dates=...")
        for filename, date_size in duplicate_dates.items():
            log.debug(f"    {filename}: {date_size}")

    # TODO add parameters ...
    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.mc.checksums', 'Log checksums',
        command_arguments=(
                CommonConsoleCommandArgument('fast_checksums', 'bool', 'True: Read max. 5 MB to create a checksum..', is_optional=True, default_value=True),
                CommonConsoleCommandArgument('return_only_duplicates', 'bool', 'True: Return only duplicates.', is_optional=True, default_value=True),
        )
    )
    def o19_debug_mc_checksums(output: CommonConsoleCommandOutput, fast_checksums: bool = True, return_only_duplicates: bool = True):
        mcs = ModCheckStore()
        if fast_checksums:
            if return_only_duplicates:
                checksums = mcs.checksums_fast_dup
            else:
                checksums = mcs.checksums_fast_all
        else:
            if return_only_duplicates:
                checksums = mcs.checksums_slow_dup
            else:
                checksums = mcs.checksums_slow_all

        output(f"Found {len(checksums)} checksums")
        log.debug(f"checksums(fast_checksums={fast_checksums}, return_only_duplicates={return_only_duplicates})=...")  # {checksums}")
        for checksum, filenames in checksums.items():
            log.debug(f"    {checksum}: '{filenames}'")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.inactive', 'inactive')
    def o19_debug_mc_disabled(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        inactive_scripts = mcs.inactive_scripts
        output(f"Found {len(inactive_scripts)} inactive scripts")
        log.debug(f"inactive_scripts={inactive_scripts}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.filetypes', 'filetypes')
    def o19_debug_mc_filetypes(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        filetypes = mcs.filetypes
        output(f"Found {len(filetypes)} different filetypes")
        log.debug(f"filetypes={filetypes}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.filetype_details', 'filetype_details')
    def o19_debug_mc_filetypes_details(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        filetype_details = mcs.filetype_details
        output(f"Found {len(filetype_details)} different filetypes")
        log.debug(f"filetype_details=...")
        for name, data in filetype_details.items():
            log.debug(f"    '{name}': '{data}'")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.mod_data', 'mod_data')
    def o19_debug_mc_mod_data(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        mod_data: Set[str] = mcs.mod_data
        output(f"Found {len(mod_data)} mod_data folders")
        log.debug(f"mod_data=...")
        for name in mod_data:
            log.debug(f"    '{name}'")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.files_to_avoid', 'Return a list of files to avoid.')
    def o19_debug_mc_files_to_avoid(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        files_to_avoid = mcs.files_to_avoid
        output(f"Found {len(files_to_avoid)} files to avoid")
        log.debug(f"files_to_avoid=...")
        for f in files_to_avoid:
            log.debug(f"    '{f}'")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.dlcs', 'dlcs')
    def o19_debug_mc_dlcs(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        available_packs, missing_packs = mcs.dlcs
        output(f"Found {len(available_packs)}/{len(missing_packs)} available / missing packs")
        log.debug(f"available_packs={available_packs}")
        log.debug(f"missing_packs={missing_packs}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.instance_managers', 'instance_managers')
    def o19_debug_mc_instance_managers(output: CommonConsoleCommandOutput):
        mcs = ModCheckStore()
        tuning_count = mcs.tuning_count
        log.debug(f"tuning_count={tuning_count}")
        output(f"Found {tuning_count} tunings")
        instance_managers = mcs.instance_managers
        output(f"Found {len(instance_managers)} instance managers")
        log.debug(f"instance_managers=...")
        for name, data in instance_managers.items():
            log.debug(f"    '{name}': '{data}'")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.mc.lazy', 'lazy')
    def o19_debug_mc_lazy(output: CommonConsoleCommandOutput):
        ssc = SelfServiceCheat()
        ssc.o19_debug_mc_filetypes(output)
        ssc.o19_debug_mc_filetypes_details(output)
        ssc.o19_debug_mc_duplicate_files(output)
        ssc.o19_debug_mc_dlcs(output)
        ssc.o19_debug_mc_disabled(output)
        ssc.o19_debug_mc_mod_data(output)
        ssc.o19_debug_mc_duplicate_dates(output)
        ssc.o19_debug_mc_files_to_avoid(output)
        ssc.o19_debug_mc_checksums(output, True, True)
        ssc.o19_debug_mc_instance_managers(output)


SelfServiceCheat()
