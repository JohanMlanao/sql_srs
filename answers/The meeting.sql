SELECT
l.meeting_id as meeting_id,
l.person_name,
l.duration_minutes,
r.person_name
FROM meetings as l
INNER JOIN meetings as r
USING (meeting_id)
WHERE l.person_name == 'Benjamin'
AND r.person_name != 'Benjamin'