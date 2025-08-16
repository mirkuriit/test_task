from sqlalchemy.dialects.postgresql import UUID, BIGINT
from sqlalchemy.orm import mapped_column as column
from sqlalchemy import text


from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Balance(Base):
    __tablename__ = "balances"

    id = column(
        UUID,
        primary_key=True,
        server_default=text('gen_random_uuid()')
    )
    user_id = column(UUID,
                     ### заглушка, в реальном проекте брали бы id cуществующих пользователей
                     server_default=text('gen_random_uuid()'))
    max_balance = column(BIGINT, nullable=False)
    current_balance = column(BIGINT, nullable=False)
