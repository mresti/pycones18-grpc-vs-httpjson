package main

import (
  "fmt"
  "net/http"

  "golang.org/x/net/context"
  "github.com/grpc-ecosystem/grpc-gateway/runtime"
  "google.golang.org/grpc"
    
  gw "github.com/mresti/pycones18-grpc-vs-httpjson/grpcgw/api"
)

func run() error {
  ctx := context.Background()
  ctx, cancel := context.WithCancel(ctx)
  defer cancel()
 
  mux := runtime.NewServeMux()
  opts := []grpc.DialOption{grpc.WithInsecure(), grpc.FailOnNonTempDialError(true)}

  urlEndpoint := "grpcapi:50051"
  err := gw.RegisterAPIHandlerFromEndpoint(ctx, mux, urlEndpoint, opts)
  if err != nil {
    fmt.Errorf("RegisterAPIHandlerFromEndpoint with info %q", urlEndpoint)
    return err
  }
  fmt.Printf("http server running... :9000 ")
  return http.ListenAndServe(":9000", mux)
}

func main() {
  if err := run(); err != nil {
    fmt.Errorf("%#v", err)
  }
}
