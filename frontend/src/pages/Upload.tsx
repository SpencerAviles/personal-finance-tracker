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

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!file || !bank || !accountName) {
      alert("Please fill in all fields.");
      return;
    }
    try {
      const uploadResult = await uploadCSV(file, bank, accountName);
      setResult(uploadResult);
      console.log(`Successfully inserted "${uploadResult.inserted}" transactions, skipped "${uploadResult.duplicates_skipped}" duplicates`);
    }
    catch (error) {
      alert("Error uploading CSV. Please try again.");
    }
  }

  return (
    <div className="max-w-lg mx-auto mt-10 px-4">
      <h1 className="text-2xl font-semibold mb-6">Upload CSV</h1>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="space-y-1">
          <label className="text-sm font-medium">Bank</label>
          <Select value={bank} onValueChange={setBank}>
            <SelectTrigger>
              <SelectValue placeholder="Select a bank" />
            </SelectTrigger>
            <SelectContent>
              {BANK_OPTIONS.map((opt) => (
                <SelectItem key={opt.value} value={opt.value}>
                  {opt.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-1">
          <label className="text-sm font-medium">Account Name</label>
          <input
            type="text"
            value={accountName}
            onChange={(e) => setAccountName(e.target.value)}
            placeholder="e.g. Chase Checking 1234"
            className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
          />
        </div>

        <div className="space-y-1">
          <label className="text-sm font-medium">CSV File</label>
          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files?.[0] ?? null)}
            className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm shadow-sm file:border-0 file:bg-transparent file:text-sm file:font-medium"
          />
        </div>

        <Button type="submit" className="w-full">
          Upload
        </Button>
      </form>

      {result && (
        <div className="mt-6 rounded-md border border-border bg-muted p-4 text-sm">
          <p className="font-medium">Upload complete</p>
          <p className="text-muted-foreground mt-1">
            {result.inserted} transactions imported, {result.duplicates_skipped} duplicates skipped.
          </p>
        </div>
      )}
    </div>
  );
}
