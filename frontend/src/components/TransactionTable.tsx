import { Transaction } from "@/api/transactions";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";

interface Props {
  transactions: Transaction[];
  onCategoryChange?: (id: number, category: string) => void;
}

export default function TransactionTable({ transactions, onCategoryChange }: Props) {
  // TODO: Render a table with columns: Date, Description, Amount, Category, Account
  // TODO: Display category as a Badge component
  // TODO: Allow clicking the category badge to edit it (calls onCategoryChange)
  // TODO: Format amount as currency (e.g. $12.34)
  return <div>Transaction table goes here</div>;
}
