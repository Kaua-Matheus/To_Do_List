"""Create User Table

Revision ID: 920c8d8125b3
Revises: 
Create Date: 2026-09-21 21:08:35.570165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '920c8d8125b3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(30), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("user")
