from pathlib import Path
import mps
import requests
from tqdm import tqdm

here = Path(__file__).absolute().parent

datadir = here / "data"


def load_sample_data(full_resolution: bool = False):
    if full_resolution:
        path = datadir / "Count00000_Point2C_ChannelBF_Seq0015.nd2"
    else:
        path = datadir / "Count00000_Point2C_ChannelBF_Seq0015.npy"

    if not path.exists():
        download_dataset(datadir=datadir, full_resolution=full_resolution)

    return mps.MPS(path)


def download(path, link, desc=None):
    if desc is None:
        desc = f"Download data to {path}"

    response = requests.get(link, stream=True)
    total_size_in_bytes = int(response.headers.get("content-length", 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True, desc=desc)

    with open(path, "wb") as handle:
        for data in response.iter_content(chunk_size=1000 * 1024):
            progress_bar.update(len(data))
            handle.write(data)
    progress_bar.close()


def download_dataset(datadir, full_resolution: bool = False, overwrite: bool = False):
    if full_resolution:
        link = "https://www.dropbox.com/scl/fi/d885qvngi3oqfdc8fnxin/Count00000_Point2C_ChannelBF_Seq0015.nd2?rlkey=yb9dmf3zj597idte89cba73wx&dl=1"
        path = datadir / "Count00000_Point2C_ChannelBF_Seq0015.nd2"
    else:
        path = datadir / "Count00000_Point2C_ChannelBF_Seq0015.npy"
        link = "https://www.dropbox.com/scl/fi/dy9e3vqyjf57bih3i36iz/Count00000_Point2C_ChannelBF_Seq0015.npy?rlkey=2415vstljhbm2lmt1b06ytxfj&&dl=1"

    if path.exists() and not overwrite:
        print(f"File {path} already exists. Skipping download.")
    else:
        Path(datadir).mkdir(exist_ok=True, parents=True)
        download(path=path, link=link)


def main():
    download_dataset(datadir=datadir, full_resolution=True)


if __name__ == "__main__":
    raise SystemExit(main())
