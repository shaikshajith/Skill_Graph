from app.queries import (
    get_candidate_skills,
    find_matching_jobs,
    get_missing_skills,
    get_company_jobs,
    get_related_skills,
    get_multi_hop_connections,
    get_all_candidates

)


def main():

    # Test 1: Candidate skills
    results = get_candidate_skills("C001")

    print("\nCandidate Skills")
    print("----------------")

    for row in results:
        print(
            f"{row['candidate']} | "
            f"{row['skill']} | "
            f"{row['category']}"
        )

    # Test 2: Job matching
    results = find_matching_jobs("C001")

    print("\nJob Matches")
    print("-----------")

    for row in results:
        print(
            f"{row['job']} | "
            f"{row['location']} | "
            f"{row['matched_skills']}/"
            f"{row['total_required']} | "
            f"{row['match_percentage']}%"
        )
    # Test 3: Missing skills
    results = get_missing_skills("C001", "J001")

    print("\nMissing Skills")
    print("--------------")

    for row in results:
        print(
            f"{row['job']} | "
            f"{row['missing_skill']} | "
            f"{row['category']}"
        )
        # Test 4: Company jobs
    results = get_company_jobs("CO001")

    print("\nCompany Jobs")
    print("------------")

    for row in results:
        print(
            f"{row['company']} | "
            f"{row['job']} | "
            f"{row['location']} | "
            f"{row['experience_level']}"
        )
        # Test 5: Related skills
    results = get_related_skills("S001")

    print("\nRelated Skills")
    print("--------------")

    for row in results:
        print(
            f"{row['skill']} -> "
            f"{row['related_skill']} | "
            f"{row['category']}"
        )
        # Test 6: Multi-hop graph traversal
    results = get_multi_hop_connections("C001")

    print("\nMulti-hop Connections")
    print("---------------------")

    for row in results:
        print(
            f"{row['candidate']} | "
            f"{row['skill']} | "
            f"{row['job']} | "
            f"{row['company']}"
        )
        # Test 7: All candidates
    results = get_all_candidates()

    print("\nAll Candidates")
    print("--------------")

    for row in results:
        print(
            f"{row['candidate_id']} | "
            f"{row['candidate']}"
        )


if __name__ == "__main__":
    main()