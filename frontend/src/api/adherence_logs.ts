import api from './axios';

export interface AdherenceLogResponse {
    id: number;
    user_id: number;
    medication_id: number;
    taken_at: string;
    status: string;
}

export const getAdherenceLogs = async(): Promise<AdherenceLogResponse[]> => {
    const response = await api.get<AdherenceLogResponse[]>('/adherence_logs');
    return response.data;
}