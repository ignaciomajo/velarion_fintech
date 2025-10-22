import { useEffect } from "react";
import { refreshToken } from "../services/auth";

export function useRefreshToken() {
  useEffect(() => {
    const interval = setInterval(() => {
      refreshToken();
    }, 60 * 60 * 1000); // 60 minutos
    return () => clearInterval(interval);
  }, []);
}
