interface ButtonProps {
    type: "button" | "submit" | "reset";
    children: React.ReactNode;
}

export default function Button({ type, children }: ButtonProps) {
    return (
        <button type={type} className="mt-6 w-full rounded-lg bg-red-600 py-3 text-sm font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
            {children}
        </button>
    );
}