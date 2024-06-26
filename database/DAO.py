from database.DB_connect import DBConnect
from model.Album import Album


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getNodi(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.AlbumId, sum(t.Milliseconds)/60000 as durata, a.Title
            from album a 
            join track t on a.AlbumId = t.AlbumId 
            group by a.AlbumId 
            having sum(t.Milliseconds)/60000 >= %s"""

        cursor.execute(query,(durata,))

        for row in cursor:
            result.append(Album(row["AlbumId"],row["Title"],row["durata"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getArchi(a1,a2):
        conn = DBConnect.get_connection()


        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as conto
from track t 
join playlisttrack p on t.TrackId = p.TrackId 
join playlisttrack p2 on p.PlaylistId =p2.PlaylistId 
join track t2 on t2.TrackId =p2.TrackId 
where t.TrackId != t2.TrackId and t.AlbumId =%s and t2.AlbumId =%s """

        cursor.execute(query,(a1,a2))

        for row in cursor:
            result=row["conto"]

        cursor.close()
        conn.close()
        return result