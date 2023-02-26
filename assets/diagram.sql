Table users {
    id integer pk
    username varchar
    email varchar
    password varchar
    first_name varchar
    last_name varchar
    is_superuser boolean
}

Table songs {
    id integer pk
    title varchar
    duration varchar
    album_id integer 
}

Ref: songs.album_id > albums.id

Table albums {
    id integer pk
    name varchar
    year integer
    user_id integer
}

Ref: albums.user_id > users.id