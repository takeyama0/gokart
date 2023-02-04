import gokart.config.config as cf

use_polars = """
: boolean
    Whether to use polars instead of pandas
"""

cf.register_option(
    "use_polars",
    False,
    use_polars,
)
