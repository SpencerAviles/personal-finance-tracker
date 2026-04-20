import { useState } from "react";
import { uploadCSV } from "@/api/transactions";
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const BANK_OPTIONS = [
  { value: "chase_checking", label: "Chase Checking" },
  { value: "chase_credit", label: "Chase Credit Card" },
  { value: "capital_one", label: "Capital One" },
  { value: "bank_of_america", label: "Bank of America" },
];

export default function Upload() {
  const [file, setFile] = useState<File | null>(null);
  const [bank, setBank] = useState<string>("");
  const [accountName, setAccountName] = useState<string>("");
  const [result, setResult] = useState<{ inserted: number; duplicates_skipped: number } | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    // TODO: Validate that file, bank, and accountName are all set
    // TODO: Call uploadCSV and store the result in state
    // TODO: Show a success message with how many transactions were inserted
  }

  return (
    <div>
      {/* TODO: Form with file input, bank selector, account name input, and submit button */}
      {/* TODO: Show result summary after successful upload */}
      <h1>Upload CSV</h1>
    </div>
  );
}
