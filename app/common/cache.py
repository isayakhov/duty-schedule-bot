from typing import List

import redis

from app.config import REDIS_DB, REDIS_HOST, REDIS_PORT

_redis_cli = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


class Cache:

    PEOPLE_TPL = "{platform}:PEOPLE:{chat_id}"
    SCHEDULE_TPL = "{platform}:SCHEDULE:{chat_id}"

    def __init__(self, redis_cli: redis.Redis) -> None:
        self.redis_cli = redis_cli

    def get_chats_by_people(self, platform: str) -> List[str]:
        return [
            key.decode("utf-8").strip().split(":")[-1]
            for key in self.redis_cli.keys(self.PEOPLE_TPL.format(platform=platform, chat_id="*"))
        ]

    def get_people(self, platform: str, chat_id: str) -> List[str]:
        cached_users = self.redis_cli.lrange(self.PEOPLE_TPL.format(platform=platform, chat_id=chat_id), 0, -1)
        return [user.decode("utf-8") for user in cached_users]

    def set_people(self, platform: str, chat_id: str, people: List[str]) -> None:
        self.remove_people(platform, chat_id)
        if people:
            self.redis_cli.rpush(self.PEOPLE_TPL.format(platform=platform, chat_id=chat_id), *people)

    def remove_people(self, platform: str, chat_id: str) -> None:
        self.redis_cli.delete(self.PEOPLE_TPL.format(platform=platform, chat_id=chat_id))

    def get_chats_by_schedules(self, platform: str) -> List[str]:
        return [
            key.decode("utf-8").strip().split(":")[-1]
            for key in self.redis_cli.keys(self.SCHEDULE_TPL.format(platform=platform, chat_id="*"))
        ]

    def get_schedule(self, platform: str, chat_id: str) -> List[str]:
        cached_schedule = self.redis_cli.lrange(self.SCHEDULE_TPL.format(platform=platform, chat_id=chat_id), 0, -1)
        return [schedule.decode("utf-8") for schedule in cached_schedule]

    def set_schedule(self, platform: str, chat_id: str, schedule: List[str]) -> None:
        self.remove_schedule(platform, chat_id)
        self.redis_cli.rpush(self.SCHEDULE_TPL.format(platform=platform, chat_id=chat_id), *schedule)

    def remove_schedule(self, platform: str, chat_id: str) -> None:
        self.redis_cli.delete(self.SCHEDULE_TPL.format(platform=platform, chat_id=chat_id))


cache = Cache(_redis_cli)
