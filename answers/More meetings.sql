WITH meetings_benjamin AS (
    SELECT meeting_id,
    rdf.person_name,
    ldf.duration_minutes
    FROM meetings AS ldf
    INNER JOIN meetings AS rdf
    USING (meeting_id)
    WHERE ldf.person_name == 'Benjamin'
    AND rdf.person_name != 'Benjamin'
)

SELECT person_name,
AVG(duration_minutes)
FROM meetings_benjamin
GROUP BY person_name
ORDER BY person_name