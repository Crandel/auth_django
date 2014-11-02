from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    """
    Command to convert all fields to utf8.
    """
    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        for row in cursor.fetchall():
            cursor.execute("ALTER TABLE %s CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;" % (row[0]))
           