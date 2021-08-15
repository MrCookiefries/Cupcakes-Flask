"""utils for the cupcake app"""

def get_cupcake_data(d):
    """returns cupcake dict"""
    return {
        "flavor": d["flavor"],
        "size": d["size"],
        "rating": d["rating"],
        "image": d.get("image")
    }
