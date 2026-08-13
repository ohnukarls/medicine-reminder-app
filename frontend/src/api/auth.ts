import api from "./axios";

export interface RegisterRequest {
    email: string;
    password: string;
    username: string;
}

export interface LoginRequest {
    email:string;
    password:string;
}

export interface LoginResponse {
    access_token: string;
    token_type: string;
}

export const register = async(
    user: RegisterRequest
): Promise<void> => {
    await api.post('/auth/register', user);
}

export const login = async(
    credentials: LoginRequest 
): Promise<LoginResponse> => {
    const response = await api.post<LoginResponse>(
        '/auth/login',
        credentials
    );
    return response.data;
}