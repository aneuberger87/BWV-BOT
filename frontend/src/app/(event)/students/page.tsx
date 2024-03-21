import { PageStudent } from "./page-student";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Schüler",
};

const Page = () => {
  return <PageStudent />;
};

export default Page;

export const revalidate = 0;
export const dynamic = "force-dynamic";
