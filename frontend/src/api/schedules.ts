import api from "./axios";

export interface ScheduleRequest {
    medication_id: number;
    recurrence_time: string;
    reminder_time: string;
    timezone: string;
}

export interface ScheduleResponse {
    id: number;
    medication_id: number;
    recurrence_time: string;
    reminder_time: string;
    timezone: string;
}

export const createSchedule = async(
    schedule: ScheduleRequest
): Promise<ScheduleResponse> => {
    const response = await api.post<ScheduleResponse>(
        '/schedules',
        schedule
    );
    return response.data;
}

export const getSchedules = async(): Promise<ScheduleResponse[]> => {
    const response = await api.get<ScheduleResponse[]>('/schedules');
    return response.data;
}   

export const updateSchedule = async(
    id: number,
    schedule: ScheduleRequest   
): Promise<ScheduleResponse> => {
    const response = await api.put<ScheduleResponse>(
        `/schedules/${id}`,
        schedule
    );
    return response.data;
}

export const deleteSchedule = async(
    id: number
): Promise<void> => {
    await api.delete(`/schedules/${id}`);
}
