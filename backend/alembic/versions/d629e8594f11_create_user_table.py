"""create user table

Revision ID: d629e8594f11
Revises: 920c8d8125b3
Create Date: 2026-09-22 19:55:37.702145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd629e8594f11'
down_revision: Union[str, Sequence[str], None] = '920c8d8125b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(30), nullable=False)
    )

    op.create_table(
        "task",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("user")