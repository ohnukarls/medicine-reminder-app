import MedicationCard from "../MedicationCard/MedicationCard";

interface MedicationListProps {
    medications: {
        id: number;
        medication_name: string;
        dosage: string;
        instructions: string;
    }[];
    onDelete: (id: number) => void;
    onUpdate: (id: number, updatedMedication: {
        medication_name: string; 
        dosage: string;
        instructions: string 
    }) => void;
}

export default function MedicationList({ medications, onDelete, onUpdate }: MedicationListProps) {
    return (
        <div>
            {medications.map((medication) => (
                <MedicationCard
                    key={medication.id}
                    medication={medication}
                    onDelete={onDelete}
                    onUpdate={onUpdate}
                />
            ))}
        </div>
    );
}