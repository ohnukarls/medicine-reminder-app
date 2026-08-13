import type { ChangeEvent } from "react";

interface InputProps {
    id: string;
    type: string;
    value: string;
    onChange: (event: ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
}

export default function Input({ id, type, value, onChange, placeholder }: InputProps) {
    return (
        <input
            id={id}
            type={type}
            value={value}
            onChange={onChange}
            placeholder={placeholder}
            className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-blue-500 focus:ring-blue-100"
        />
    );
}