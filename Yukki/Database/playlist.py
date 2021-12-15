from typing import Dict, List, Union

from Yukki import db

playlistdb_dangdut = db.playlistdangdut
playlistdb_reggae = db.playlistreggae
playlistdb_indopop = db.playlistindopop
playlistdb_rock = db.playlistrock
playlistdb_hiphop = db.playlisthiphop
playlistdb_alquran = db.playlistalquran
playlistdb_djlokal = db.playlistdjlokal
playlistdb_kristen = db.playlistkristen


async def _get_playlists(chat_id: int, type: str) -> Dict[str, int]:
    if type == "Dangdut":
        xd = playlistdb_dangdut
    elif type == "Reggae":
        xd = playlistdb_reggae
    elif type == "IndoPop":
        xd = playlistdb_indopop
    elif type == "Rock":
        xd = playlistdb_rock
    elif type == "HipHop":
        xd = playlistdb_hiphop
    elif type == "Al-Qur'an":
        xd = playlistdb_alquran
    elif type == "DjLokal":
        xd = playlistdb_djlokal
    elif type == "Kristen":
        xd = playlistdb_kristen
    _notes = await xd.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_playlist_names(chat_id: int, type: str) -> List[str]:
    _notes = []
    for note in await _get_playlists(chat_id, type):
        _notes.append(note)
    return _notes


async def get_playlist(
    chat_id: int, name: str, type: str
) -> Union[bool, dict]:
    name = name
    _notes = await _get_playlists(chat_id, type)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_playlist(chat_id: int, name: str, note: dict, type: str):
    name = name
    _notes = await _get_playlists(chat_id, type)
    _notes[name] = note
    if type == "Dangdut":
        xd = playlistdb_dangdut
    elif type == "Reggae":
        xd = playlistdb_reggae
    elif type == "IndoPop":
        xd = playlistdb_indopop
    elif type == "Rock":
        xd = playlistdb_rock
    elif type == "HipHop":
        xd = playlistdb_hiphop
    elif type == "Al-Qur'an":
        xd = playlistdb_alquran
    elif type == "DjLokal":
        xd = playlistdb_djlokal
    elif type == "Kristen":
        xd = playlistdb_kristen
    await xd.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_playlist(chat_id: int, name: str, type: str) -> bool:
    notesd = await _get_playlists(chat_id, type)
    name = name
    if type == "Dangdut":
        xd = playlistdb_dangdut
    elif type == "Reggae":
        xd = playlistdb_reggae
    elif type == "IndoPop":
        xd = playlistdb_indopop
    elif type == "Rock":
        xd = playlistdb_rock
    elif type == "HipHop":
        xd = playlistdb_hiphop
    elif type == "Al-Qur'an":
        xd = playlistdb_alquran
    elif type == "DjLokal":
        xd = playlistdb_djlokal
    elif type == "Kristen":
        xd = playlistdb_kristen
    if name in notesd:
        del notesd[name]
        await xd.update_one(
            {"chat_id": chat_id}, {"$set": {"notes": notesd}}, upsert=True
        )
        return True
    return False
