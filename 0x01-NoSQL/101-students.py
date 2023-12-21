#!/usr/bin/env python3
"""
Top students by avg
"""


def top_students(mongo_collection):
    """ top_students.
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])