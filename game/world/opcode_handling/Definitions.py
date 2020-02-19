from utils.constants.OpCodes import OpCode
from utils.Logger import Logger

from game.world.opcode_handling.handlers.AuthSessionHandler import AuthSessionHandler
from game.world.opcode_handling.handlers.PingHandler import PingHandler
from game.world.opcode_handling.handlers.CharEnumHandler import CharEnumHandler
from game.world.opcode_handling.handlers.CharCreateHandler import CharCreateHandler
from game.world.opcode_handling.handlers.CharDeleteHandler import CharDeleteHandler
from game.world.opcode_handling.handlers.ChatHandler import ChatHandler
from game.world.opcode_handling.handlers.PlayerLoginHandler import PlayerLoginHandler
from game.world.opcode_handling.handlers.NameQueryHandler import NameQueryHandler
from game.world.opcode_handling.handlers.TimeQueryHandler import TimeQueryHandler
from game.world.opcode_handling.handlers.LogoutRequestHandler import LogoutRequestHandler
from game.world.opcode_handling.handlers.WorldTeleportHandler import WorldTeleportHandler
from game.world.opcode_handling.handlers.AreaTriggerHandler import AreaTriggerHandler
from game.world.opcode_handling.handlers.SpeedCheatHandler import SpeedCheatHandler
from game.world.opcode_handling.handlers.ZoneUpdateHandler import ZoneUpdateHandler
from game.world.opcode_handling.handlers.BugHandler import BugHandler
from game.world.opcode_handling.handlers.TextEmoteHandler import TextEmoteHandler
from game.world.opcode_handling.handlers.MovementHandler import MovementHandler


HANDLER_DEFINITIONS = {
    OpCode.CMSG_AUTH_SESSION: AuthSessionHandler.handle,
    OpCode.CMSG_PING: PingHandler.handle,
    OpCode.CMSG_CHAR_ENUM: CharEnumHandler.handle,
    OpCode.CMSG_CHAR_CREATE: CharCreateHandler.handle,
    OpCode.CMSG_CHAR_DELETE: CharDeleteHandler.handle,
    OpCode.CMSG_MESSAGECHAT: ChatHandler.handle,
    OpCode.CMSG_PLAYER_LOGIN: PlayerLoginHandler.handle,
    OpCode.CMSG_NAME_QUERY: NameQueryHandler.handle,
    OpCode.CMSG_QUERY_TIME: TimeQueryHandler.handle,
    OpCode.CMSG_LOGOUT_REQUEST: LogoutRequestHandler.handle,
    OpCode.CMSG_WORLD_TELEPORT: WorldTeleportHandler.handle,
    OpCode.MSG_MOVE_TELEPORT_CHEAT: WorldTeleportHandler.handle,
    OpCode.MSG_MOVE_WORLDPORT_ACK: WorldTeleportHandler.handle_ack,
    OpCode.SMSG_MOVE_WORLDPORT_ACK: WorldTeleportHandler.handle_ack,
    OpCode.CMSG_AREATRIGGER: AreaTriggerHandler.handle,
    OpCode.MSG_MOVE_SET_RUN_SPEED_CHEAT: SpeedCheatHandler.handle,
    OpCode.MSG_MOVE_SET_SWIM_SPEED_CHEAT: SpeedCheatHandler.handle,
    OpCode.MSG_MOVE_SET_ALL_SPEED_CHEAT: SpeedCheatHandler.handle,
    OpCode.MSG_MOVE_SET_WALK_SPEED: SpeedCheatHandler.handle,
    OpCode.MSG_MOVE_SET_TURN_RATE_CHEAT: SpeedCheatHandler.handle,
    OpCode.CMSG_ZONEUPDATE: ZoneUpdateHandler.handle,
    OpCode.CMSG_BUG: BugHandler.handle,
    OpCode.CMSG_TEXT_EMOTE: TextEmoteHandler.handle,

    OpCode.MSG_MOVE_HEARTBEAT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_UNROOT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_ROOT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_SET_PITCH: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_SET_FACING: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_STOP_SWIM: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_SWIM: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_SET_WALK_MODE: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_SET_RUN_MODE: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_STOP_PITCH: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_PITCH_DOWN: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_PITCH_UP: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_STOP_TURN: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_TURN_LEFT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_TURN_RIGHT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_JUMP: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_STOP_STRAFE: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_STRAFE_RIGHT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_STRAFE_LEFT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_STOP: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_BACKWARD: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_START_FORWARD: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_COLLIDE_REDIRECT: MovementHandler.handle_movement_status,
    OpCode.MSG_MOVE_COLLIDE_STUCK: MovementHandler.handle_movement_status
}


class Definitions(object):

    @staticmethod
    def get_handler_from_packet(world_session, opcode):
        try:
            opcode_name = OpCode(opcode)
            if opcode_name in HANDLER_DEFINITIONS:
                return HANDLER_DEFINITIONS.get(OpCode(opcode))
            else:
                Logger.warning('[%s] Received %s OpCode but is not handled.' % (world_session.client_address[0],
                                                                                opcode_name))
        except ValueError:
            Logger.error('[%s] Received unknown OpCode (%u)' % (world_session.client_address[0], opcode))
        return None
