import { downloadInputExcelAsBuffer } from "@/lib/download";

export const GET = async () => {
  const buffer = await downloadInputExcelAsBuffer("studentsList");
  if (buffer === null)
    return new Response("File does not exist", { status: 404 });

  return new Response(buffer, {
    headers: {
      "Content-Type": "application/octet-stream",
      "Content-Disposition": `attachment; filename="studentsList.xlsx"`,
    },
  });
};

export const dynamic = "force-dynamic";
