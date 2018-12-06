import sys

def get_argument():
    """
    Get model id argument.

    Returns
    -------
    int
        Model id.
    """
    if (len(sys.argv) < 2):
        print('No model passed.')
        sys.exit(1)
    return sys.argv[1]
