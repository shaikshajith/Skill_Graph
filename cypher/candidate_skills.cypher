MATCH (c:Candidate {id: $candidate_id})
      -[:HAS_SKILL]->
      (s:Skill)
RETURN
    c.name AS candidate,
    s.name AS skill,
    s.category AS category
ORDER BY s.name;