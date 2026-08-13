import api from "./axios";

export interface MedicationRequest {
    medication_name: string;
    dosage: string;
    instructions: string;    
}

export interface MedicationResponse {
    id: number;
    medication_name: string;
    dosage: string;
    instructions: string;    
}

export const createMedication = async(
    medication: MedicationRequest
): Promise<MedicationResponse> => { 
    const response = await api.post<MedicationResponse>(
        '/medications',
        medication
    );
    return response.data;
}

export const getMedications = async(): Promise<MedicationResponse[]> => {
    const response = await api.get<MedicationResponse[]>('/medications');
    return response.data;
}

export const updateMedication = async(
    id: number,
    medication: MedicationRequest
): Promise<MedicationResponse> => {
    const response = await api.put<MedicationResponse>(
        `/medications/${id}`,
        medication
    );
    return response.data;
}

export const deleteMedication = async(
    id: number
): Promise<void> => {
    await api.delete(`/medications/${id}`);
}
