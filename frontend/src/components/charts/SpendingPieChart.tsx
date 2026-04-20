import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { CategorySummary } from "@/api/transactions";

interface Props {
  data: CategorySummary[];
}

const COLORS = [
  "#6366f1", "#f59e0b", "#10b981", "#ef4444",
  "#3b82f6", "#8b5cf6", "#ec4899", "#14b8a6",
];

export default function SpendingPieChart({ data }: Props) {
  // TODO: Render a responsive pie chart using the data prop
  // TODO: Each slice represents a category, sized by total amount
  // TODO: Use COLORS array to color each slice
  // TODO: Show a tooltip with category name and dollar amount on hover
  return <div>Pie chart goes here</div>;
}
