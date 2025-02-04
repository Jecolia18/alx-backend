#!/usr/bin/env python3
"""helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """helper function"""
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)
