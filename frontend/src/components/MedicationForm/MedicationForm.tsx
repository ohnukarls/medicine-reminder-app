import { useState } from 'react';
import { createMedication, getMedications, updateMedication, deleteMedication } from "../../api/medications";


export default function MedicationForm() {
    const [medicationName, setMedicationName] = useState('');
    const [dosage, setDosage] = useState('');
    const [instructions, setInstructions] = useState('');

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const medication = {
            medication_name: medicationName,
            dosage: dosage,
            instructions: instructions,
        };

        console.log(medication);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="medication-name">
                    Medication Name
                </label>

                <input
                    type="text"
                    id="medication-name"
                    value={medicationName}
                    onChange={(e) => setMedicationName(e.target.value)}
                    placeholder="Enter medication name"
                />
            </div>

            <div>
                <label htmlFor="dosage">
                    Dosage
                </label>

                <input
                    type="text"
                    id="dosage"
                    value={dosage}
                    onChange={(e) => setDosage(e.target.value)}
                    placeholder="Enter dosage"
                />
            </div>

            <div>
                <label htmlFor="instructions">
                    Instructions
                </label>

                <textarea
                    id="instructions"
                    value={instructions}
                    onChange={(e) => setInstructions(e.target.value)}
                    placeholder="Enter instructions"
                />
            </div>

            <button type="submit">
                Add Medication
            </button>
        </form>
    );
}