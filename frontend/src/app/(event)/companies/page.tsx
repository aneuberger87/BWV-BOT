import { PageCompany } from "./page-company";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Firmen",
};

const Page = () => {
  return (
    <>
      <PageCompany />
    </>
  );
};

export default Page;
