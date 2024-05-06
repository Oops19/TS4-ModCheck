#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict, List, Tuple
from mod_check.mod_check_singleton import ModCheckSingleton

from mod_check.modinfo import ModInfo
try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class TS4Stats(metaclass=ModCheckSingleton):

    # noinspection PyMethodMayBeStatic
    def get_dlcs(self) -> Tuple[List[str], List[str]]:
        """
        @return: Tuple with List of available and missing DLCs
        """
        available_packs = []
        missing_packs = []
        try:
            from sims4.common import Pack, is_available_pack
            for index in Pack:
                pack_name = Pack(index).name
                if is_available_pack(index):
                    available_packs.append(pack_name)
                else:
                    missing_packs.append(pack_name)
            available_packs.sort()
            missing_packs.sort()
        except Exception as e:
            log.error(f"get_dlcs: Oops: {e}", throw=True)
        return available_packs, missing_packs

    def count_tunings(self) -> int:
        """
        @return: Number of tunings / descriptions
        """
        num_tunings = 0
        try:
            import sims4
            import sims4.tuning
            import sims4.tuning.serialization
            num_tunings = len(sims4.tuning.serialization.tuning_class_set)
        except Exception as e:
            log.error(f"num_tunings: Oops: {e}", throw=True)
        return num_tunings

    def get_instance_managers(self) -> Dict[str, Tuple[int, float]]:
        """
        @return: Dict with instance_manager_name: (sum_types, load_time)
        """
        instance_managers: Dict[str, Tuple[int, float]] = dict()
        try:
            log.debug(f'tuning: INSTANCE_MANAGER_NAME, TYPES, LOAD_TIME')
            from server_commands.tuning_commands import get_managers
            managers = get_managers()
            for manager in managers:
                instance_manager = managers.get(manager, None)
                instance_managers.update({f"{instance_manager.TYPE.name}": (len(instance_manager.types), instance_manager.load_time)})
        except Exception as e:
            log.error(f"instance_managers: Oops: {e}", throw=True)
        return instance_managers