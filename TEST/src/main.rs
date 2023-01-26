use axum::{http::header::HeaderMap, routing::get, Router};

async fn home(headers: HeaderMap) -> &'static str {
    dbg!(headers);
    "Hello World"
}

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::TRACE)
        .init();
    let app = Router::new()
        .route("/", get(home))
        .layer(tower_http::trace::TraceLayer::new_for_http());

    // run it with hyper on localhost:3000
    tracing::warn!("starting");
    axum::Server::bind(&"0.0.0.0:5000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
