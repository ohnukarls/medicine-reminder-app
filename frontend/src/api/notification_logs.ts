import api from "./axios";

export interface NotificationLogResponse {
    id: number;
    schedule_id: number;
    status: string;
    message: string;
    sent_at: string;
}


export const getNotificationLogs = async(): Promise<NotificationLogResponse[]> => {
    const response = await api.get<NotificationLogResponse[]>('/notification_logs');
    return response.data;
}