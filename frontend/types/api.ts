export type HealthResponse = {
  status: "healthy" | "degraded" | string;
  app: string;
  version: string;
  dependencies: {
    database: boolean;
    redis: boolean;
  };
};
