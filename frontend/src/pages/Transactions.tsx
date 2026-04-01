import { useEffect, useState } from "react";
import { Transaction, getTransactions, updateTransactionCategory } from "@/api/transactions";
import TransactionTable from "@/components/TransactionTable";

export default function Transactions() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [month, setMonth] = useState<number | undefined>();
  const [year, setYear] = useState<number | undefined>();

  useEffect(() => {
    // TODO: Fetch transactions whenever month or year filter changes
    // TODO: Store results in state
  }, [month, year]);

  async function handleCategoryChange(id: number, category: string) {
    // TODO: Call updateTransactionCategory with the id and new category
    // TODO: Update the transaction in local state so the UI reflects the change immediately
  }

  return (
    <div>
      {/* TODO: Month and year filter dropdowns */}
      {/* TODO: TransactionTable with transactions and handleCategoryChange */}
      <h1>Transactions</h1>
    </div>
  );
}
