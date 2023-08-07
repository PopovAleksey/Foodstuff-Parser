from database.connector import Connector
from dto.statistic_dto import StatisticDto
from repository.statistic_status import StatisticStatus


class StatisticRepository(Connector):
    def set_status(self, statistic_dto: StatisticDto):
        self.get_cursor().execute(
            "UPDATE statistic SET status = ? WHERE store_id = ? AND category_id = ?",
            (
                statistic_dto.status,
                statistic_dto.store_id,
                statistic_dto.category_id
            )
        )
        self.commit()

    def get_in_progress(self) -> StatisticDto:
        cursor = self.get_cursor()
        cursor.execute(
            "SELECT * FROM statistic WHERE status = ? LIMIT 1",
            (StatisticStatus.IN_PROGRESS.value,)
        )

        data = cursor.fetchone()

        if data is None:
            raise RuntimeError('Statistic is empty! Parse all')

        return StatisticDto(
            store_id=int(data['store_id']),
            category_id=str(data['category_id']),
            last_product_ean=str(data['last_product_ean']),
            num_paginator_page=int(data['num_paginator_page']),
            status=StatisticStatus.IN_PROGRESS.value
        )