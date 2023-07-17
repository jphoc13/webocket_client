import asyncio

class Clienttests:

    def heartbeat_test(self, message, current, previous):
        assert message == "This is a heartbeat", "Meesage for heartbeat is wrong"
        if previous:
            assert (current - previous) < 2, 'Heart beat not coming fast enough, possible ' \
                                             'connection issue'
        return None
