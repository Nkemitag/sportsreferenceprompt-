from typing import Dict


def build_head_to_head_matrix(data: Dict[str, Dict[str, Dict[str, int]]]) -> None:
    """
    Prints a head-to-head matrix showing number of wins only.
    Rows = team
    Columns = opponent
    """

    teams = sorted(data.keys())

    # Header
    header = ["Tm"] + teams
    print("\t".join(header))

    for team in teams:
        row = [team]
        for opponent in teams:
            if team == opponent:
                row.append("--")
            else:
                wins = data.get(team, {}).get(opponent, {}).get("W")
                row.append(str(wins) if wins is not None else "")
        print("\t".join(row))


if __name__ == "__main__":
    # Example structure (values shown only for demonstration)
    sample_data = {
        "BRO": {"BSN": {"W": 10}, "CHC": {"W": 15}},
        "BSN": {"BRO": {"W": 12}, "CHC": {"W": 13}},
        "CHC": {"BRO": {"W": 7}, "BSN": {"W": 9}},
    }

    build_head_to_head_matrix(sample_data)
