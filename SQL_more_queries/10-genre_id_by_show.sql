-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre.
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs JOIN tv_show_genres AS tvsg
ON tvs.id = tvsg.show_id
ORDER BY tvs.title ASC, tvsg.genre_id ASC;