from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Dangdut",
                callback_data=f"play_playlist {user_id}|{type}|Dangdut",
            ),
            InlineKeyboardButton(
                text=f"Reggae",
                callback_data=f"play_playlist {user_id}|{type}|Reggae",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"IndoPop",
                callback_data=f"play_playlist {user_id}|{type}|IndoPop",
            ),
            InlineKeyboardButton(
                text=f"Rock",
                callback_data=f"play_playlist {user_id}|{type}|Rock",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"HipHop",
                callback_data=f"play_playlist {user_id}|{type}|HipHop",
            ),
            InlineKeyboardButton(
                text=f"Al-Qur'an",
                callback_data=f"play_playlist {user_id}|{type}|Al-Qur'an",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"DjLokal",
                callback_data=f"play_playlist {user_id}|{type}|DjLokal",
            ),
            InlineKeyboardButton(
                text=f"Kristen",
                callback_data=f"play_playlist {user_id}|{type}|Kristen",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Kembali",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ Dangdut",
                callback_data=f"add_playlist {videoid}|{type}|Dangdut",
            ),
            InlineKeyboardButton(
                text=f"✚ Reggae",
                callback_data=f"add_playlist {videoid}|{type}|Reggae",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ IndoPop",
                callback_data=f"add_playlist {videoid}|{type}|Indo Pop",
            ),
            InlineKeyboardButton(
                text=f"✚ Rock",
                callback_data=f"add_playlist {videoid}|{type}|Rock",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ HipHop",
                callback_data=f"add_playlist {videoid}|{type}|HipHop",
            ),
            InlineKeyboardButton(
                text=f"✚ Al-Qur'an",
                callback_data=f"add_playlist {videoid}|{type}|Al-Qur'an",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ DjLokal",
                callback_data=f"add_playlist {videoid}|{type}|DjLokal",
            ),
            InlineKeyboardButton(
                text=f"✚ Kristen",
                callback_data=f"add_playlist {videoid}|{type}|Kristen",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Kembali", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Dangdut", callback_data=f"check_playlist {type}|Dangdut"
            ),
            InlineKeyboardButton(
                text=f"Reggae", callback_data=f"check_playlist {type}|Reggae"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"IndoPop", callback_data=f"check_playlist {type}|IndoPop"
            ),
            InlineKeyboardButton(
                text=f"Rock", callback_data=f"check_playlist {type}|Rock"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"HipHop",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"Al-Qur'an",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"DjLokal",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"Kristen", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Daftar Putar Antrian Checkout", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Periksa Daftar Putar", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Ya! Menghapus",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="Tidak!", callback_data=f"close"),
        ],
    ]
    return buttons
