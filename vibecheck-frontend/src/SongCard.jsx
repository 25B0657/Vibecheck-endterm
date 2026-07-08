import placeholder from "./assets/placeholder.png";

function SongCard({ song }) {
  return (
    <a
      href={song.url}
      target="_blank"
      rel="noopener noreferrer"
      style={{
        textDecoration: "none",
        color: "black",
      }}
    >
      <div
        style={{
          border: "1px solid #ccc",
          borderRadius: "10px",
          padding: "15px",
          width: "250px",
          height: "340px",
          textAlign: "center",
          cursor: "pointer",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          boxSizing: "border-box",
        }}
      >
        <img
          src={song.cover_image || placeholder}
          alt={song.song}
          width="180"
          height="180"
          style={{
            objectFit: "cover",
            borderRadius: "8px",
            marginBottom: "15px",
          }}
        />

        <h3
          title={song.song}
          style={{
            width: "100%",
            margin: "0 0 10px 0",
            whiteSpace: "nowrap",
            overflow: "hidden",
            textOverflow: "ellipsis",
          }}
        >
          {song.song}
        </h3>

        <p
          title={song.artist}
          style={{
            width: "100%",
            margin: "0",
            color: "#555",
            whiteSpace: "nowrap",
            overflow: "hidden",
            textOverflow: "ellipsis",
          }}
        >
          {song.artist}
        </p>
      </div>
    </a>
  );
}

export default SongCard;