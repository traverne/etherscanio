from .base import Module


class Statistics(Module):
    module = "stats"

    def get_native_total_supply(self):
        payload = {"action": "ethsupply"}

        self.modulize(payload)
        return self.client.request(payload)

    def get_merged_native_total_supply(self):
        payload = {"action": "ethsupply2"}

        self.modulize(payload)
        return self.client.request(payload)

    def get_native_last_price(self):
        payload = {"action": "ethprice"}

        self.modulize(payload)
        return self.client.request(payload)

    def get_ethereum_node_size(
        self,
        start_date: str,
        end_date: str,
        client_type: str = "geth",
        sync_mode: str = "default",
        sort: str = "desc",
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)
        self.assertions.client(client_type)
        self.assertions.sync(sync_mode)

        payload = {
            "action": "chainsize",
            "startdate": start_date,
            "enddate": end_date,
            "clienttype": client_type,
            "syncmode": sync_mode,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_total_node_count(self):
        payload = {"action": "nodecount"}

        self.modulize(payload)
        return self.client.request(payload)

    def get_daily_network_transaction_fee(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "dailytxnfee",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_daily_new_address_count(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "dailynewaddress",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_daily_network_utialization(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "dailynetutilization",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_average_network_hashrate(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "dailyavghashrate",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_daily_transaction_count(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "dailytx",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_daily_average_network_difficulty(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "dailyavgnetdifficulty",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)

    def get_native_historical_prices(
        self, start_date: str, end_date: str, sort: str = "desc"
    ):
        self.assertions.sorting(sort)
        self.assertions.date(start_date)
        self.assertions.date(end_date)

        payload = {
            "action": "ethdailyprice",
            "startdate": start_date,
            "enddate": end_date,
            "sort": sort,
        }

        self.modulize(payload)
        return self.client.request(payload)
