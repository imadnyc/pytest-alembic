import sqlalchemy as sa
from alembic import op
from sqlalchemy import text

revision = "aaaaaaaaaaaa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(text("CREATE SCHEMA meow"))

    op.create_table(
        "foo",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="meow",
    )


def downgrade():
    op.drop_table("foo", schema="meow")
    op.execute("DROP SCHEMA meow")
