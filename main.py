import psycopg2
import os
from datetime import datetime

DATABASE_URL = os.environ["DATABASE_URL"]
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS study_logs (
    id SERIAL PRIMARY KEY,
    user_id TEXT,
    subject TEXT,
    content TEXT,
    created_at TIMESTAMP
);
""")
conn.commit()

@bot.command()
async def log(ctx, subject, *, content):
    cur.execute(
        "INSERT INTO study_logs (user_id, subject, content, created_at) VALUES (%s,%s,%s,%s)",
        (str(ctx.author.id), subject, content, datetime.now())
    )
    conn.commit()
    await ctx.send("記録しました")
