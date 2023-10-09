import matplotlib.pyplot as plt
from pathlib import Path
import shutil


def rcparams():
    if shutil.which("latex"):
        return {
            "text.usetex": True,
            "font.family": "sans-serif",
            "font.sans-serif": ["Helvetica"],
        }
    return {}


plt.rcParams.update(rcparams())

here = Path(__file__).absolute().parent

datadir = here / "data"


mps_paths = (
    datadir / "Count00000_Point2C_ChannelBF_Seq0015.npy",
    datadir / "bayK/control_10690/20211126-GCaMP80HCF20-BayK_Stream_B01_s1_TL-20.npy",
)

mps_paths_orig = (
    datadir / "Count00000_Point2C_ChannelBF_Seq0015.nd2",
    datadir / "bayK/control_10690/20211126-GCaMP80HCF20-BayK_Stream_B01_s1_TL-20.tif",
)

first_beat_start = (40, 150)
first_beat_end = (85, 350)

DEFAULT_REFERENCE_FRAMES = (162, 747)

# assert mps_path.is_file(), f"File {mps_path} does not exist"
DEFAULT_SPACING = (1, 5)
figdir = here / "figures"
figdir.mkdir(exist_ok=True)

results_dir = here / "results"
results_dir.mkdir(exist_ok=True)
DB_PATH = here / "data.xlsx"


recording_pattern = "{date}-{dye}-{drug}_Stream_B01_s1_{channel}"
