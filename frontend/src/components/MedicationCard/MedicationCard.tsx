import { useState } from 'react';
interface MedicationCardProps {
    medication: {
        id: number;
        medication_name: string;
        dosage: string;
        instructions: string;
    };
    onDelete: (id: number) => void;
    onUpdate: (id: number, updatedMedication: { medication_name: string; dosage: string; instructions: string }) => void;
}

export default function MedicationCard({ medication, onDelete, onUpdate }: MedicationCardProps) {
    const [isEditing, setIsEditing] = useState(false);
    const [editedMedication, setEditedMedication] = useState({
        medication_name: medication.medication_name,
        dosage: medication.dosage,
        instructions: medication.instructions,
    });
    return (
        <div>
            <h2>{medication.medication_name}</h2>
            <p>{medication.dosage}</p>
            <p>{medication.instructions}</p>

            <button onClick={() => setIsEditing(!isEditing)}>
                Edit
            </button>
            <button onClick={() => onDelete(medication.id)}>
                Delete
            </button>
        </div>
    );
}